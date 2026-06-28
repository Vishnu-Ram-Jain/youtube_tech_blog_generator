from crew import run


def main():

    print("=" * 60)

    print("YouTube Blog Generator")

    print("=" * 60)

    topic = input("\nEnter Topic : ")

    channel = input("Enter Channel Handle : ")

    run(

        topic=topic,

        channel=channel

    )


if __name__ == "__main__":

    main()