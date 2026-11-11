from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location("hak_akses_admin", "9_12_hak_akses_admin.py")
modul = module_from_spec(spec)
spec.loader.exec_module(modul)

Admin = modul.Admin

admin = Admin("Vrysa", "Dewi", 18)

admin.describe_user()
admin.privileges.show_privileges()