class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        if not A:
            return A

        stack = []

        dirname = []

        for c in A:
            if c == '/':
                if len(dirname) > 0:
                    n = ''.join(dirname)
                
                    if n == '.':
                        dirname = []
                        continue
                    elif n == '..':
                        if len(stack) > 0:
                            stack.pop()
                    else:
                        stack.append(n)
                
                dirname = []
            else:
                dirname.append(c)

        if len(dirname) > 0:
            n = ''.join(dirname)

            if n == '.':
                pass
            elif n == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(n)

        return '/' + '/'.join(stack)


print(Solution().simplifyPath('/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/..') == '/ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/wrm/grm/ach/jsy/dic/ggz/smq/yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/llb/tud/olc/zns/fiv/eeu/fex/kke/eng/bow/uvz/jmz/hwb/ids/dwj/aqu/erf')
print(Solution().simplifyPath('/../') == '/')
print(Solution().simplifyPath('') == '')
print(Solution().simplifyPath('/') == '/')
print(Solution().simplifyPath('/aaa') == '/aaa')
print(Solution().simplifyPath('/home/') == '/home')
print(Solution().simplifyPath('/a/./b/../../c/') == '/c')

if __name__ == '__main__':
    assert(Solution().simplifyPath("/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/..") == "/ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/wrm/grm/ach/jsy/dic/ggz/smq/yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/llb/tud/olc/zns/fiv/eeu/fex/kke/eng/bow/uvz/jmz/hwb/ids/dwj/aqu/erf")
    assert(Solution().simplifyPath("/foo///////home/../") == "/foo")
    assert(Solution().simplifyPath("/foo//home") == "/foo/home")
    assert(Solution().simplifyPath("/../") == "/")
    assert(Solution().simplifyPath("/home/..") == "/")
    assert(Solution().simplifyPath("/home/../") == "/")
    assert(Solution().simplifyPath("/home") == "/home")
    assert(Solution().simplifyPath("/home/") == "/home")
    assert(Solution().simplifyPath("/a/./b/../../c/") == "/c")

