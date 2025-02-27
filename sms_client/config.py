import toml
import pathlib


def load_server_config() -> dict[str:]:
    """Загрузка конфигурации сервера из файла TOML."""
    file_path = pathlib.Path(__file__).parent.parent.joinpath('config.toml')
    try:
        with open(file_path, 'r') as f:
            config = toml.load(f)

        res = dict(host=config['servers']['server1']['host'],
                    port=config['servers']['server1']['port'])
        # print(res)
        return res
    except FileNotFoundError:
        print("Файл конфигурации не найден.")
        return dict()


class ServerConfig:
    host: str
    port: int

    def __init__(self):
        conf = load_server_config()
        self.host = conf['host']
        self.port = conf['port']


def load_user_config() -> dict[str:str]:
    """Загрузка конфигурации пользователей из файла TOML."""
    file_path = pathlib.Path(__file__).parent.parent.joinpath('config.toml')
    try:
        with open(file_path, 'r') as f:
            config = toml.load(f)

        res = dict(username=config['users']['user1']['username'],
                    password=config['users']['user1']['password'])

        return res
    except FileNotFoundError:
        print("Файл конфигурации не найден.")
        return dict()


class UserConfig:
    username: str
    password: str

    def __init__(self):
        conf = load_user_config()
        self.username = conf['username']
        self.password = conf['password']
