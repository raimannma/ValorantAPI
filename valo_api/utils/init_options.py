from typing import Any, Dict


class InitOptions:
    """A class to simplify the initialization of objects."""

    @classmethod
    def from_dict(cls, **kwargs: Dict[str, Any]):
        """Create instance from relevant keywords in dictionary.

        Instead of passing exactly the arguments defined by the class' __init__,
        this allows to pass a dictionary of many more values and the function will
        then only pass the correct arguments to the class' __init__.

        Example:
            >>> from valo_api.utils.init_options import InitOptions
            >>> class SomeClass(InitOptions):
            ...
            ...     def __init__(self, arg1, arg2):
            ...         self.arg1 = arg1
            ...         self.arg2 = arg2
            ...
            ...
            >>> many_args = {"arg1": 1, "arg2": 2, "arg3": 3}
            ... # This will raise an exception because __init__ does not expect arg3!
            >>> try:
            ...     SomeClass(**many_args)
            ... except TypeError:
            ...     pass
            ... # However this will work:
            >>> something = SomeClass.from_dict(**many_args)

        Args:
            **kwargs: Keyword arguments matching the constructor's variables.

        Returns:
            An instance of the class.
        """
        init_keys = (
            cls.__init__.__code__.co_varnames
        )  # Access the init functions arguments
        kwargs = {
            key: kwargs[key] for key in init_keys if key in kwargs
        }  # Select all elements in kwargs, that are also arguments of the init function
        return cls(**kwargs)
