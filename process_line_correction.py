def string_corr (filename):
  print "Correcting string line breaks in " + filename
  file = open(filename,"r")
  lines = file.readlines()
  file.close()

  file = open(filename,"w")
  
  line_break = 0
  last_line = "last line"
  for line in lines:
    is_comment = line.strip().find("#")

    if is_comment != 0:
        
      if line_break > 0:
        line = last_line + line
      
      line_break = line.find("\\\n")
      
      if line_break > 0:
        last_line = line.replace("\\\n", " \" + \"")
        line_break = 1
      
      for x in range(0, 20):
        line = line.replace("  \" + \"", " \" + \"")
        line = line.replace("\" + \" ", "\" + \"")
      
      line = line.replace("^ \" + \"", "^\" + \"")
      line = line.replace("\" + \"", "\" + \n\"")

    if line_break < 1:
      line = line.strip()
      file.write("%s\n"%line)  
  file.close()
