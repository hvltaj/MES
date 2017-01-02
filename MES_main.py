from mes.mes import *
import numpy as np
import os.path

cli_parser = CLIParser().args
input_file_name = cli_parser.i_filename
output_file_name = cli_parser.o_filename

data = FileParser(input_file_name)
data.parse_file()

H_global = np.array(fill_h_global(data.elements))
P_global = np.array([item * -1 for item in fill_p_global(data.elements)])

mes_result = np.linalg.solve(H_global, P_global)
# print(H_global)
# print(P_global)
# print(result)

result = "H Global:\n"
result += str(H_global)
result += "\n----------------------\n"
result += "P Global:\n"
result += str(P_global)
result += "\n----------------------\n"
result += "RESULT\n"
result += str(mes_result)

with open(output_file_name, "w") as fn:
    fn.write(result)