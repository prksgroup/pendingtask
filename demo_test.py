from  pywinauto import Application
app=Application().start(r"c:\windows\system32\notepad.exe")
dlg=Application().connect(path=r"c:\windows\system32\notepad.exe")
dlg=app.window()
dlg.print_control_identifiers()
dlg.menu_select("File->save as")

this_one=app.window(title="Save As")
this_one.Edit1.set_edit_text("Sample")
this_one.save.click()



