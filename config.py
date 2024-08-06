import os


class PathConfig:
    # 项目绝对根目录
    ABS_ROOT_PATH = os.path.abspath(os.getcwd())


class RouterConfig:
    # 合法pathname列表
    VALID_PATHNAME = ["/", "/login", "/user-management"]

    PATHNAME_PERMISSION = {
        '/user-management': '用户管理'
    }


class MenuConfig:
    def __init__(self):
        self.menu_items = {
            '用户管理': {
                "component": "Item", 
                "props": {
                    "key": "用户管理",
                    "title": "用户管理",
                    "icon": "antd-team",
                    "href": "/user-management",
                }
            }
        }

    def return_menu_items(self, permission: list):
        '''
        根据用户权限返回对应的菜单项
        '''

        user_menu_items = [
            self.menu_items.get(i) for i in permission
        ]
        _user_menu_items = [
            i for i in user_menu_items if i
        ]
        return _user_menu_items

