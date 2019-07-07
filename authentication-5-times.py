from django.contrib.auth import authenticate
import time
count=0
bool=false

while count<5:
 user = authenticate(username='form_user',password='form_pass')
 if user is not None:
  return render(request, 'users/template.html', context)
  bool=true
 else:
  print('Try again')
  count +=1

if bool=false:
  print('Try again later!')
  time.sleep(100)
