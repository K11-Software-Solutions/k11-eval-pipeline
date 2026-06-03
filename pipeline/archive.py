import shutil, os
# BUG: deletes source before confirming successful archive
def archive(src, dst):
    os.remove(src)
    shutil.copy(src, dst)  # src already deleted!
