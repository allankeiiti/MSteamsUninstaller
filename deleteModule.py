from os import system, scandir, sep

def scanWinUserFolders(inputDir):
   # Essa função escaneia a pasta local de usuários e retorna uma lista dos usuários logados
   try:
      userList = []
      notAddList = ['Default', 'Default User', 'Todos os Usuários', 'Usuário Padrão', 'desktop.ini', 'All Users', 'Public']
      with scandir(path = inputDir) as folders:
         for users in folders:
            if users.path.split(sep)[-1] not in notAddList:
               userList.append(users.path.split(sep)[-1])

      return userList
   except PermissionError:
      pass
   except FileNotFoundError:
      print('ERRO: {} não foi localizado.'.format(inputDir))

inputDir = r'C:\\Users'
userList = scanWinUserFolders(inputDir)

for user in userList:
   teamsTaskKill = r'taskkill /im teams.exe /f'
   uninstallCommand = r'C:\\Users\\{}\\AppData\\Local\\Microsoft\\Teams\\Update.exe --uninstall'.format(user)
   deleteFolder = r'rmdir /S /Q C:\\Users\\{}\\AppData\\Local\\Microsoft\\Teams'.format(user)
   system(teamsTaskKill)
   print(uninstallCommand)
   system(uninstallCommand)
   print(deleteFolder)
   system(deleteFolder)