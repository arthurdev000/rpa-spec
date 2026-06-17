# RPA Specification

This repository contains the RPA (RISC-V Processor Architecture) Specification.

## Building the Documentation

### Prerequisites

Install the required Python packages:

```bash
pip install -r requirements.txt
```

For PDF output, you also need:
- A LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- `latexmk` command

For diagrams:
- [Graphviz](https://graphviz.org/) (for graphviz diagrams)
- [PlantUML](https://plantuml.com/) (for UML diagrams)

### Build HTML

```bash
cd doc
make html
```

The output will be in `doc/_build/html/`.

### Build PDF

```bash
cd doc
make latexpdf
```

The output will be in `doc/_build/latex/`.

## Directory Structure

```
rpa-spec/
├── doc/                    # Documentation source files
│   ├── conf.py             # Sphinx configuration
│   ├── index.rst           # Main index
│   ├── overview/           # Overview documents
│   ├── api/                # API specification
│   ├── appendix/           # Appendix (glossary, history)
│   └── figure/             # Diagrams and figures
├── headers/                # Reference header files
├── examples/               # Example code
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## License

- **Documentation**: [CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt)
- **Code examples and headers**: [Apache-2.0](LICENSES/Apache-2.0.txt)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Copyright

Copyright 2026 Shanghai HappyFull Technologies