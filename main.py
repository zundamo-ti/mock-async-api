import uvicorn


def main():
    app_path = "src.mock_async_api.app:app"
    uvicorn.run(app_path, host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
