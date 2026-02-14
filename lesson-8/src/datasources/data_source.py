class Source:
    def load_data(self) -> None:
        raise NotImplementedError("the 'load_data' method must be implemented by a subclass.")

    def get_text(self) -> str:
        raise NotImplementedError("the 'get_text' method must be implemented by a subclass.")
