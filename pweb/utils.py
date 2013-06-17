from pweb.globe import get_globe

def build_menu(active):
  menus=[]
  globe_settings=get_globe()
  for menu in globe_settings["menus"]:
    if 'active' in globe_settings["menus"][menu]:
      globe_settings["menus"][menu]['active']=False
    if active == menu:
      globe_settings["menus"][menu]['active']=True
    menus.append( globe_settings["menus"][menu] )
  return menus

