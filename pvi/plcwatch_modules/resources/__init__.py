import os
import tkinter as tk

_script_dir = os.path.dirname(os.path.abspath(__file__))
_pics = ( 'app', 'array', 'boolean', 'cpu', 'date_and_time', 'device',
      'i8', 'i16', 'i32', 'lreal', 'real', 'string', 'wstring', 
      'struct', 'task', 'time', 'time', 'u8', 'u16', 'u32', 'variable',
      'wstring' )

icon_storage = { str(k) : f'{_script_dir}\\{k}.ico' for k in _pics }
image_files = {str(k) : f'{_script_dir}\\{k}.png' for k in _pics }


