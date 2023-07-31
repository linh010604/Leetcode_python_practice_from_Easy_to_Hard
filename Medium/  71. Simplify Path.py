class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if len(path) == 0 :
            return '/'

        if path[0] != '/' :
            path = '/' + path

        oldpath = ""
        while oldpath != path :
            oldpath = path
            path = path.replace("""//""",'/')

        idx = 0

        oldpath = ""

        while idx < len(path) :
            if path[idx] == '/' :
                idx += 1
                s = ""
                while idx < len(path) and path[idx] != '/' :
                    s += path[idx]
                    idx += 1

                if s != '..' and s != '.' :
                    oldpath += '/' + s
                elif s == '..' :
                    i = len(oldpath) - 1
                    while len(oldpath) > 0 and i >= 0 and oldpath[i] != '/' :
                        i -= 1

                    oldpath = oldpath[:i]


        while len(oldpath) > 1 and oldpath[-1] == '/':
            oldpath = oldpath[:-1]
        
        if len(oldpath) == 0 or oldpath[0] != '/' :
            oldpath = "/" + oldpath

        return oldpath
