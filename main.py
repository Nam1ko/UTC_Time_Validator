from application.time_service import TimeService
from infrastructure.source_repository import SourceRepository
from presentation.console import Console

def main():
    repository = SourceRepository()
    service = TimeService()

    console = Console(repository, service)
    console.run()

if __name__ == "__main__":
    main()

# C:\Users\yuram\Downloads\TimeTest.txt
# https://www.utctime.net/