[Setup]
AppName=MyApp
AppVersion=1.0
DefaultDirName={pf}\MyApp
DefaultGroupName=MyApp
OutputDir=Output
OutputBaseFilename=MyAppSetup

[Files]
Source: "F:\PYTHON-APP\PYTHON-GUI\FORM1\dist\Frm_menu.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\PYTHON-APP\PYTHON-GUI\FORM1\form_csdl.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\PYTHON-APP\PYTHON-GUI\FORM1\employee_management.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\PYTHON-APP\PYTHON-GUI\FORM1\employee_add.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\PYTHON-APP\PYTHON-GUI\FORM1\db_connection.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\PYTHON-APP\PYTHON-GUI\FORM1\find_form.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\PYTHON-APP\PYTHON-GUI\FORM1\app_icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MyApp"; Filename: "{app}\Frm_menu.exe"
