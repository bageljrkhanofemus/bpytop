from GPUmodules import GPUmodule as Gpu
from GPUmodules import env

from gpu.common import Backend, gpu_data


class Ricks_lab(Backend):
	platform = ["Linux"]
	vendor = ["amd", "nvidia"]

	def __init__(self):
		env.GUT_CONST.check_env()
		self.gpus = Gpu.GpuList()

	def find_devices(self):
		self.gpus.set_gpu_list(clinfo_flag=True)
		self.avail_gpus = self.gpus.list_gpus(compatibility=Gpu.GpuItem.GPU_Comp.Readable)
		self.num_gpus = self.gpus.num_gpus()["total"]

	def get_current_usage(self) -> list[gpu_data]:
		self.avail_gpus.read_gpu_sensor_set(Gpu.GpuItem.SensorSet.Monitor)
		data = []
		for gpu in self.gpus:
			data.append(gpu_data(gpu.get_params_value("loading"), gpu.get_params_value("mem_loading")))
		return data


if __name__ == '__main__':
	gpus = Ricks_lab()
	gpus.find_devices()
	print(gpus.get_current_usage())
