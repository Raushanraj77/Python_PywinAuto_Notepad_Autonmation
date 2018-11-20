from pywinauto.application import Application
app = Application().start("notepad.exe")
app.UntitledNotepad.Edit.type_keys("This is Kushan Amarasiri - Python Rocks...", with_spaces = True)
app.UntitledNotepad.menu_select("File->Save As")
dlg = app.window(title='Save As')
dlg.Edit.type_keys("kushan")
dlg.Save.click()
dlg.Save.click()
app.UntitledNotepad.menu_select("File->Exit")
