def string_handling(student_name):
    filename="textfile.txt"
    with open(file=filename,mode="r") as file:
        found= False
        new_list =[]
        for line in file:
            if  line.startswith(f"{student_name}"):
              print(f"{student_name} IS PRESENT")
              found=True
            else:
                new_list.append(f"{line}")
        if found:
            with open(file=filename,mode="w") as file:
               file.writelines(new_list)
        elif not found:
            print(f"{student_name} IS NOT IN TEXT FILE")    


                
string_handling(student_name="RAM")              