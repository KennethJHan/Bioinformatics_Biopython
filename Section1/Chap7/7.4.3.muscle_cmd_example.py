#7.4.3.muscle_cmd_example.py 

from Bio.Align.Applications import MuscleCommandline 

muscle_exe = "/Users/jhan/etc/muscle/muscle3.8.31_i86darwin64"  # MUSCLE의 실행경로를 알려준다. MUSCLE 프로그램의 경로는 독자여러분들의 경로에 따라 다르므로 자신의 환경에 맞게 설정하자.
cmd_line = MuscleCommandline(muscle_exe, input="HBA.all.fasta", out="HBA.aln", clw=" ") # clw 옵션을 주기위해 clw=" " 를 넣었다. 

print(cmd_line) 

stdout, stderr = cmd_line()
