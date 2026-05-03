# Chatbot Evolution Roadmap

This document describes a gradual evolution path for the chatbot built in these tutorials, moving from a local experimental project to a more serious and extensible conversational platform.

## Current State

Up to lesson 12, the project already supports important concepts:

- chat conversation management
- session introduction
- multiple sessions through a `SessionManager`
- Streamlit UI
- RAG integration
- document ingestion through CLI tools

However, there are still some structural gaps before considering the chatbot a more complete application:

- sessions are not persisted, so conversations are lost when the application stops
- there is currently a bug/limitation in the RAG integration because multiple conversations effectively depend on a shared collection instead of having explicit collection ownership
- frontend and backend are still tightly coupled
- user management does not exist yet
- authorization and tenancy are not present
- the current UI is still a tutorial UI, not a production-style chat interface

## Guiding Principles

The roadmap should follow a gradual and coherent architecture-first approach:

1. fix the current RAG/session boundary
2. introduce persistence
3. refine the domain model where needed
4. expose stable APIs
5. add user management
6. enforce authorization
7. improve the UX on top of stable foundations

The goal is to avoid building advanced UI or authentication features on top of an unstable in-memory architecture.

## Recommended Evolution Order

### 1. Fix the current RAG/session bug first

Before introducing persistence or APIs, the first step should be to fix the current limitation in the relationship between chat sessions and RAG collections.

At the moment, the application supports multiple sessions, but the RAG side still behaves as if there were a shared collection. This means the session boundary is incomplete.

The immediate goal should be:

- make the association between chat session and RAG collection explicit
- avoid accidental sharing when isolation is expected
- define clearly whether a session owns a collection or references one

For the next step of the tutorials, the simplest rule is:

- **1 session = 1 RAG collection/space**

This is not necessarily the final model, but it is the clearest way to make session isolation correct.

Later, the model can evolve toward reusable or shared knowledge spaces, but that should be an explicit feature, not an accidental side effect.

### 2. Introduce persistence immediately

Persistence should be the next major step.

Today, if the chatbot is stopped, all sessions and messages are lost. This is the biggest limitation of the current architecture.

A good first choice is **SQLite**, because it is:

- simple to introduce
- easy to explain in a tutorial
- sufficient for local development
- easy to migrate later to PostgreSQL

The first persisted entities should be:

- sessions
- messages
- RAG spaces / collections
- source metadata
- session settings

Suggested initial schema:

#### `users`

- `id`
- `username`
- `email` nullable at first
- `password_hash` nullable at first
- `created_at`

#### `sessions`

- `id`
- `user_id` nullable at first
- `title`
- `knowledge_space_id`
- `model_provider`
- `model_name`
- `temperature`
- `system_prompt`
- `rag_enabled`
- `created_at`
- `updated_at`

#### `messages`

- `id`
- `session_id`
- `role`
- `content`
- `metadata_json`
- `created_at`

#### `knowledge_spaces`

- `id`
- `name`
- `vector_collection_name`
- `embedding_provider`
- `embedding_model`
- `created_at`

#### `sources`

- `id`
- `knowledge_space_id`
- `type`
- `original_name`
- `uri`
- `status`
- `created_at`

### 3. Move configuration from global-only to layered configuration

Today most configuration is in `config.yaml`. That is still useful, but no longer enough.

The recommended direction is to introduce three levels of configuration:

#### Application defaults

Stored in `config.yaml`:

- default LLM provider
- default model
- default embedding provider/model
- database path
- vector database settings

#### Session settings

Stored in the database for each session:

- provider
- model
- temperature
- system prompt
- RAG enabled/disabled
- associated knowledge space

#### Runtime request options

Optional future overrides for single requests.

This keeps `config.yaml` as the source of technical defaults, while allowing each session to have its own behavior.

This also works well for both UI and text mode:

- the UI can edit these settings visually
- the CLI can expose commands to change them

### 4. Introduce backend APIs for chat and RAG

Once persistence and the domain model are stable, it makes sense to separate frontend and backend.

Recommended backend capabilities:

#### Chat API

- list sessions
- create session
- rename session
- delete session
- list messages
- send message

#### RAG API

- create knowledge space
- list knowledge spaces
- upload documents
- ingest URLs
- list sources
- delete sources

Suggested technology:

- **FastAPI** for the backend

At that point:

- the current Streamlit UI can progressively become an API client
- the CLI can also become a client of the same APIs
- chat logic and ingestion logic become reusable across interfaces

### 5. Add local registered users

After persistence and APIs, introduce user registration and login.

This is the right moment because:

- ownership can already be represented in the database
- sessions and knowledge spaces can be tied to a user
- the architecture is ready for protected APIs

Initial features:

- user registration
- login
- password hashing
- session cookie or token-based authentication

### 6. Add authorization and tenancy

After user registration, enforce ownership rules.

Minimum rules:

- a user can only see their own sessions
- a user can only see their own knowledge spaces
- a user can only upload sources into their own spaces

Possible future evolution:

- shared spaces
- organizations or teams
- admin role

This is the real transition from a personal app to a multi-user system.

### 7. Redesign the user experience

The new UX should come after persistence, APIs, and auth are already in place.

Target direction:

- layout similar to ChatGPT or OpenWebUI
- left sidebar with sessions/conversations
- main chat area
- bottom composer
- settings panel
- knowledge management page for uploads and indexing

This avoids rebuilding the UI multiple times while the backend is still changing.

## Proposed Lesson Sequence

### Lesson 13 — Persistence with SQLite

- introduce repositories
- persist sessions and messages
- persist knowledge spaces and sources
- restore data on startup
- keep `Session` and `SessionManager` as core concepts
- associate each session with a RAG space

### Lesson 14 — Per-session settings

- move model/provider/temperature/system prompt into session settings
- keep `config.yaml` as defaults
- allow current CLI and UI to read and modify those settings

### Lesson 15 — Backend APIs

- introduce FastAPI
- add chat endpoints
- add RAG ingestion endpoints
- progressively decouple UI from backend logic

### Lesson 16 — Registered users

- user registration
- login
- data ownership
- protected APIs

### Lesson 17 — Authorization and tenancy

- enforce per-user isolation
- prepare for roles and sharing models

### Lesson 18 — New UX

- ChatGPT/OpenWebUI-style interface
- sessions/conversations sidebar
- knowledge management view
- settings editor
- upload from browser

## Notes on Naming

At this stage, it is not necessary to remove `Session` or `SessionManager`.

In the current codebase:

- `Session` already represents a chat instance with its own history
- `SessionManager` already manages multiple chat instances
- `Conversation` appears to be the object that stores the sequence of exchanged messages inside a session

So, in practice, `Conversation` is not a replacement for `Session`; it is part of a `Session`.

A clearer interpretation is:

- `Session` = the top-level chat container selected by the user
- `Conversation` = the message history inside that session
- `SessionManager` = the component that creates, selects, lists, and deletes sessions

This means there is no need to rename everything immediately.

A reasonable evolution is:

- keep `Session` and `SessionManager`
- persist them
- associate each `Session` with a RAG space
- only reconsider naming later if the domain model truly requires it

This avoids introducing conceptual churn without functional value.

## Summary

Recommended priority:

1. fix session/RAG collection isolation
2. persistent sessions and RAG spaces
3. per-session settings
4. backend APIs
5. registered users
6. authorization and tenancy
7. modern UX

This order gives the project a clean path from tutorial code to a more serious chatbot platform.
