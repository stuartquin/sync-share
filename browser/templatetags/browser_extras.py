from django import template

register = template.Library()

def browse_path(value, current_path):
    # {'is_dir': True, 'full_path': u'/home/stuart/Sync/vimwiki', 'is_image': False, 'name': u'vimwiki'}
    path = "/browser?path="
    if value["is_dir"]:
        path = path + value["full_path"]
    else:
        path = path + current_path
        path = path + "&view=" + value["full_path"]

    return path
        

register.filter("browse_path", browse_path)
