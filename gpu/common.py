from dataclasses import dataclass
from typing import List


@dataclass
class gpu_data:
	usage: int
	memory_load: int


class Backend():
	platform: List[str]
	vendor: List[str]

	def get_current_usage(self) -> List[gpu_data]:
		pass
