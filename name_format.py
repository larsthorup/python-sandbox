def format_name(first_name, middle_inital, last_name):
  """
  Format a name for display from parts of a name
  Returns a string 
  """
  if middle_inital == '':
    return first_name + ' ' + last_name
  else:
    return first_name + ' ' + middle_inital + '. ' + last_name

print(format_name('Sju', 'G', 'Thorup'))
print(format_name('Lars', '', 'Thorup'))