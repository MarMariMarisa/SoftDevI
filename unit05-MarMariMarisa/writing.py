def plot_grades(infile, first_name, last_name):
    def plot_grades(filename,first,last):
    found = False
    try:
        with open(filename) as file:
            for line in file:
                fields = line.strip().split(',')
                if fields[1] == first and fields[0] == last:
                    found = True
                    count = 2
                    plotter.init(first + " " + last, "Grade Item", "Score")
                    while len(fields) > count:  
                        try:
                            plotter.add_data_point(float(fields[count])) 
                        except ValueError:
                            plotter.add_data_point(0)
                        count += 1         
            plotter.plot()
            file.close()
            return found
    except:
        raise FileNotFoundError
