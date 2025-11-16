.PHONY: env train eval figs tests clean dist

env:
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

train:
python scripts/train_backbone.py --config configs/model_distilbert.yaml

eval:
python scripts/evaluate.py --config configs/data_emotion.yaml

figs:
python scripts/gen_figures.py --output docs/figures

tests:
pytest -q

clean:
rm -rf .venv __pycache__ */__pycache__

# Create a zipped bundle of the project for easy sharing/download
dist:
	mkdir -p dist
	git archive --format=zip --prefix=depressor/ -o dist/depressor.zip HEAD:depressor
