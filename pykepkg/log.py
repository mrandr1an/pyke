class Log:
    def __init__(self,file_name):
        self.file_name="pykelog.txt"
    def write_to_log(self,*argv):
        with open(self.file_name, "a") as f:
            for line in argv:
                f.write(line + "\n")
                f.close
    def write_example(self,file_name, *argv):
        with open(file_name, 'a') as f:
            for example in argv:
                f.write(example  + "\n")

    def make_exercise(self,file_name, word):
        with open(file_name,'r') as f:
            lines = f.readlines()
            exercise_file_name = word + ".txt"
            with open(exercise_file_name, 'a') as f2:
                for line in lines:
                    f2_line = line.replace(word,"______")
                    word.replace(" ", "")
                    if str(word) in line:
                        f2.write(f2_line + "\n")
                    else:
                        pass
                        self.write_to_log("Could not make exercise word not found: " + word)
                        self.write_to_log(line)
                f2.close()
                f.close()



