import argparse
from loguru import logger

from .language_processors import get_processor

def run_application(lang):
    from .visualizer.web import application
    application.app.processor = get_processor(lang) # Set processor behaviour adapted to language for application
    application.app.run(debug=True)


def main(pattern, code, lang, args=None):
    if args and args.web:
        run_application(lang)
        return

    processor = get_processor(lang) # Get processor behaviour adapted to language
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
    parser = argparse.ArgumentParser()

    parser.add_argument("--web", action="store_true")
    parser.add_argument("--lang", choices=['python', 'java'], required=True, help="Specify the language (python/java)")

    parser.add_argument("pattern")
    parser.add_argument("code")

    args = parser.parse_args()
    main(args.pattern, args.code, args.lang, args)
