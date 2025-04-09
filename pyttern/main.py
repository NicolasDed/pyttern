import argparse

from .language_processors import get_processor

def run_application():
    from .visualizer.web import application
    application.app.run(debug=True)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--web", action="store_true", help="Launch the web application")
    parser.add_argument("--lang", choices=['python', 'java'], help="Specify the language (python/java)")

    parser.add_argument("pattern", nargs="?", help="Pattern file path")
    parser.add_argument("code", nargs="?", help="Code file path")

    args = parser.parse_args()

    if args and args.web:
        run_application()
        return
    
    if not args.lang or not args.pattern or not args.code:
        print("You must specify --lang, pattern file, and code file when not running the web application.")
        return

    processor = get_processor(args.lang) # Get processor behaviour adapted to language
    pattern = args.pattern
    code = args.code

    try:
        pattern_tree = processor.generate_tree_from_file(pattern)
        code_tree = processor.generate_tree_from_file(code)
    except Exception as e:
        print(e)
        return

    fsm = processor.create_fsm(pattern_tree)

    simu = processor.create_simulator(fsm, code_tree)

    listener = processor.create_listener()

    simu.add_listener(listener)
    simu.start()

    while len(simu.states) > 0:
        simu.step()
    print(simu.match_set.matches)

if __name__ == "__main__":
    main()
