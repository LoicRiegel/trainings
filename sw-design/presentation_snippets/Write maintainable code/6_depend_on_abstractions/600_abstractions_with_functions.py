from abc import ABC

class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

        @abstractmethod
        def prepare_export(self, video_data: str) -> None:
            """Prepares video data for exporting."""
            raise NotImplementedError

        @abstractmethod
        def do_export(self, folder: Path) -> None:
            """Exports the video data to a folder."""
            raise NotImplementedError


# Classic OO factory with classes

class VideoExporterFactory:
    """Factory to create video exporters.
    The factory doesn't maintain any of the instances it creates.
    """

    @staticmethod
    def get_video_exporter() -> VideoExporter:
        """Returns a new video exporter."""


# same thing with functions

from typing import Callable

# Represents a function that takes in no argument and that returns a VideoExporter object
ExporterFactoryFn = Callable[[], VideoExporter]
