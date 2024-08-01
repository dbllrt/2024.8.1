import h5py

# 文件路径
file_path = "F:/data.hdf"

# 打开HDF5文件
with h5py.File(file_path, 'r') as file:
    # 显示文件结构
    def print_attrs(name, obj):
        print(f"{name}: {obj}")


    file.visititems(print_attrs)

    # 读取并显示具体数据集
    dataset_name = 'data'  # 替换为你要读取的数据集名称
    data = file[dataset_name][:]
    print(data)
