import os
import platform
import ctypes

def hide_file(file_path):
    system_name = platform.system()
    
    if system_name == "Windows":
        # On Windows, use ctypes to set the file's attribute to hidden
        try:
            FILE_ATTRIBUTE_HIDDEN = 0x02
            attrs = ctypes.windll.kernel32.GetFileAttributesW(file_path)
            if attrs == -1:
                raise ctypes.WinError()
            if not attrs & FILE_ATTRIBUTE_HIDDEN:
                ctypes.windll.kernel32.SetFileAttributesW(file_path, attrs | FILE_ATTRIBUTE_HIDDEN)
            #print(f"File '{file_path}' has been hidden successfully on Windows.")
        except Exception as e:
            print(f"Failed to hide file on Windows: {e}")
    
    else:
        # On Unix-like systems, rename the file to start with a dot
        directory, filename = os.path.split(file_path)
        hidden_file_path = os.path.join(directory, f".{filename}")
        try:
            os.rename(file_path, hidden_file_path)
            #print(f"File '{file_path}' has been hidden successfully on {system_name}.")
        except Exception as e:
            print(f"Failed to hide file on {system_name}: {e}")

# Example usage:
hide_file("C:\\Users\\chris\\package.zip")
