from __future__ import annotations

from pathlib import Path
import textwrap
import nbformat as nbf

OUT = Path("06_Starter_Notebooks/ready_to_teach")
OUT.mkdir(parents=True, exist_ok=True)

HEADER = """from __future__ import annotations
import json, platform, random
from pathlib import Path
import numpy as np
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
print('Python:', platform.python_version())
print('Working directory:', Path.cwd())
"""

LESSONS = [
    {
        "id": "N01", "file": "python_trace_and_debug.ipynb", "sessions": "3-8",
        "title": "Python Trace and Debug",
        "target": "Trace state changes, repair programs, validate input, and verify behaviour with tests.",
        "concepts": ["trace variables after every executed statement", "distinguish syntax, runtime, and logic errors", "validate boundaries and malformed input", "use assertions and small test cases"],
        "entry": ["Predict a loop's output before running it.", "State one loop invariant.", "Give one boundary case and one malformed-input case."],
        "code": """values = [3, -1, 4, 0, 2]
total = count = 0
trace = []
for value in values:
    if value > 0:
        total += value
        count += 1
    trace.append((value, total, count))
print(trace)
assert total == 9 and count == 3

def safe_average(values):
    cleaned = [float(v) for v in values if v is not None]
    if not cleaned:
        raise ValueError('no usable values')
    return sum(cleaned) / len(cleaned)
assert safe_average([1, 2, None, 3]) == 2.0
""",
        "independent": "Build a CSV-row validator with required-key checks, numeric conversion, human-readable errors, and at least five tests."
    },
    {
        "id": "N02", "file": "statistics_and_metrics.ipynb", "sessions": "17-20",
        "title": "Statistics and Metrics Agreement",
        "target": "Make hand, NumPy, and scikit-learn calculations agree.",
        "concepts": ["population versus sample variance", "confusion-matrix orientation", "precision, recall, specificity, F1", "metric choice depends on error cost"],
        "entry": ["Compute a mean without a calculator.", "Define false positive and false negative.", "Explain why accuracy may mislead."],
        "code": """from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
x = np.array([2., 4., 4., 4., 5., 5., 7., 9.])
mean = x.sum() / len(x)
variance = ((x - mean) ** 2).sum() / len(x)
assert np.isclose(mean, x.mean()) and np.isclose(variance, x.var())
y_true = np.array([1,1,1,1,0,0,0,0,0,0])
y_pred = np.array([1,1,0,1,1,0,0,0,1,0])
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
manual = {'accuracy':(tp+tn)/(tp+tn+fp+fn),'precision':tp/(tp+fp),'recall':tp/(tp+fn),'specificity':tn/(tn+fp)}
manual['f1'] = 2*manual['precision']*manual['recall']/(manual['precision']+manual['recall'])
print(manual)
assert np.isclose(manual['f1'], f1_score(y_true, y_pred))
""",
        "independent": "Implement a validated metric function for tp/fp/fn/tn, including zero-denominator policy and balanced accuracy."
    },
    {
        "id": "N03", "file": "linear_logistic_models.ipynb", "sessions": "13-16",
        "title": "Linear and Logistic Models",
        "target": "Interpret residuals, probabilities, coefficients, and decision thresholds.",
        "concepts": ["linear output versus sigmoid probability", "residual analysis", "threshold is a decision rule", "split before fitting"],
        "entry": ["Classify two tasks as regression or classification.", "Define residual.", "Predict what lowering a threshold does to recall."],
        "code": """import pandas as pd
from sklearn.datasets import make_regression, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, f1_score
X, y = make_regression(n_samples=240, n_features=3, noise=12, random_state=SEED)
Xtr, Xva, ytr, yva = train_test_split(X, y, test_size=.25, random_state=SEED)
reg = LinearRegression().fit(Xtr, ytr)
pred = reg.predict(Xva)
print('RMSE', mean_squared_error(yva, pred) ** .5, 'residual mean', (yva-pred).mean())
X, y = make_classification(n_samples=500, n_features=6, weights=[.72,.28], random_state=SEED)
Xtr, Xva, ytr, yva = train_test_split(X, y, test_size=.3, stratify=y, random_state=SEED)
clf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
p = clf.predict_proba(Xva)[:,1]
print(pd.DataFrame([{'threshold':t,'f1':f1_score(yva,p>=t),'positives':int((p>=t).sum())} for t in [.2,.35,.5,.65,.8]]))
""",
        "independent": "Compare a constant baseline, logistic regression, and one alternative model under one fixed validation design."
    },
    {
        "id": "N04", "file": "trees_and_ensembles.ipynb", "sessions": "24-26",
        "title": "Trees and Ensembles",
        "target": "Diagnose depth, compare bagging and boosting, and explain bias/variance behaviour.",
        "concepts": ["impurity and split selection", "depth controls capacity", "bagging reduces variance", "boosting is sequential"],
        "entry": ["Describe a pure node.", "Predict train/validation behaviour as depth rises.", "Contrast forest and boosting."],
        "code": """import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import f1_score
X,y = make_classification(n_samples=700,n_features=12,n_informative=6,weights=[.65,.35],random_state=SEED)
Xtr,Xva,ytr,yva = train_test_split(X,y,test_size=.3,stratify=y,random_state=SEED)
rows=[]
for depth in [1,2,3,5,8,None]:
    m=DecisionTreeClassifier(max_depth=depth,random_state=SEED).fit(Xtr,ytr)
    rows.append({'depth':str(depth),'train_f1':f1_score(ytr,m.predict(Xtr)),'val_f1':f1_score(yva,m.predict(Xva))})
print(pd.DataFrame(rows))
for name,m in {'forest':RandomForestClassifier(n_estimators=80,random_state=SEED),'boost':GradientBoostingClassifier(random_state=SEED)}.items():
    m.fit(Xtr,ytr); print(name,f1_score(yva,m.predict(Xva)))
""",
        "independent": "Repeat with grouped or time-aware validation and one controlled hyperparameter experiment."
    },
    {
        "id": "N05", "file": "numpy_pandas_audit.ipynb", "sessions": "39-42",
        "title": "NumPy and Pandas Data Audit",
        "target": "Audit schema, missingness, duplicates, distributions, groups, and leakage risks before modelling.",
        "concepts": ["one row/entity/prediction", "identifier versus feature", "duplicate row versus duplicate entity", "plots must answer a diagnostic question"],
        "entry": ["Name an identifier column.", "State one missingness risk.", "Give one assertion that should stop a pipeline."],
        "code": """import pandas as pd
rng=np.random.default_rng(SEED)
df=pd.DataFrame({'id':[f'R{i:03d}' for i in range(120)],'group':rng.choice(list('ABC'),120),'age':rng.normal(16,1.5,120),'hours':rng.gamma(2,2,120),'device':rng.choice(['desktop','tablet','phone'],120),'target':rng.integers(0,2,120)})
df.loc[rng.choice(df.index,8,replace=False),'hours']=np.nan
df=pd.concat([df,df.iloc[[3]]],ignore_index=True)
audit={'shape':df.shape,'duplicate_rows':int(df.duplicated().sum()),'duplicate_ids':int(df.id.duplicated().sum()),'missing':df.isna().sum().to_dict(),'dtypes':df.dtypes.astype(str).to_dict()}
print(json.dumps(audit,indent=2))
assert audit['duplicate_rows']==1 and audit['missing']['hours']==8
""",
        "independent": "Produce audit.json, two labelled diagnostic plots, five assertions, and a leakage-risk memo for an unfamiliar CSV."
    },
    {
        "id": "N06", "file": "sklearn_mixed_pipeline.ipynb", "sessions": "41-44",
        "title": "Leakage-Safe Mixed Scikit-learn Pipeline",
        "target": "Build mixed preprocessing, group-aware validation, a baseline, and a validated submission.",
        "concepts": ["fit preprocessing inside the pipeline", "group-aware splitting", "unknown-category handling", "validate ID order and prediction range"],
        "entry": ["Locate leakage in a pre-split scaler.", "Explain handle_unknown='ignore'.", "Define first valid baseline."],
        "code": """import pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
rng=np.random.default_rng(SEED); n=400
df=pd.DataFrame({'id':[f'P{i:04d}' for i in range(n)],'school':rng.choice([f'S{i:02d}' for i in range(10)],n),'device':rng.choice(['desktop','phone','tablet'],n),'hours':rng.gamma(2,2,n),'late':rng.beta(1.5,5,n)})
df['target']=rng.binomial(1,1/(1+np.exp(-(-.8-.25*df.hours+2*df.late+(df.device=='phone')*.3))))
features=['device','hours','late']; groups=df.school
tr,va=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=SEED).split(df[features],df.target,groups))
pre=ColumnTransformer([('num',Pipeline([('imp',SimpleImputer(strategy='median')),('scale',StandardScaler())]),['hours','late']),('cat',OneHotEncoder(handle_unknown='ignore'),['device'])])
pipe=Pipeline([('pre',pre),('model',LogisticRegression(max_iter=1000))]).fit(df.loc[tr,features],df.loc[tr,'target'])
p=pipe.predict_proba(df.loc[va,features])[:,1]
assert not(set(groups.iloc[tr]) & set(groups.iloc[va]))
submission=pd.DataFrame({'id':df.loc[va,'id'].to_numpy(),'prediction':p})
assert submission.id.is_unique and submission.prediction.between(0,1).all()
print('F1',f1_score(df.loc[va,'target'],p>=.5),submission.head())
""",
        "independent": "Add one justified feature and one alternative model while keeping the split and evaluation fixed."
    },
    {
        "id": "N07", "file": "pytorch_mlp.ipynb", "sessions": "45-47",
        "title": "PyTorch MLP Training Loop",
        "target": "Create tensors, loaders, a model, train/validate loops, and a best-checkpoint record.",
        "concepts": ["tensor shape and dtype", "train versus eval mode", "zero_grad/forward/loss/backward/step", "validation uses no_grad"],
        "entry": ["State the expected input and label dtypes.", "Order the six training-loop steps.", "Explain a device mismatch."],
        "code": """import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
torch.manual_seed(SEED); device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
X,y=make_moons(n_samples=400,noise=.2,random_state=SEED)
Xtr,Xva,ytr,yva=train_test_split(X,y,test_size=.25,stratify=y,random_state=SEED)
loader=DataLoader(TensorDataset(torch.tensor(Xtr,dtype=torch.float32),torch.tensor(ytr,dtype=torch.long)),batch_size=32,shuffle=True)
model=nn.Sequential(nn.Linear(2,16),nn.ReLU(),nn.Linear(16,2)).to(device)
opt=torch.optim.Adam(model.parameters(),lr=.02); loss_fn=nn.CrossEntropyLoss()
for _ in range(5):
    model.train()
    for xb,yb in loader:
        xb,yb=xb.to(device),yb.to(device); opt.zero_grad(); loss=loss_fn(model(xb),yb); loss.backward(); opt.step()
model.eval()
with torch.no_grad():
    logits=model(torch.tensor(Xva,dtype=torch.float32,device=device)); acc=(logits.argmax(1).cpu()==torch.tensor(yva)).float().mean().item()
print('validation accuracy',acc); assert acc>.75
""",
        "independent": "Close the example and rebuild the complete train/validate/checkpoint workflow, then test one controlled regularisation change."
    },
    {
        "id": "N08", "file": "opencv_structural_baseline.ipynb", "sessions": "48",
        "title": "OpenCV Structural Baseline",
        "target": "Expose preprocessing stages and measure connected components and contours.",
        "concepts": ["thresholding and morphology", "connected components", "contour area/perimeter/bounding box", "evaluate across source styles"],
        "entry": ["Predict how noise affects thresholding.", "Define a connected component.", "Name one source-style shift."],
        "code": """import cv2
img=np.zeros((180,240),dtype=np.uint8)
cv2.circle(img,(60,80),28,255,-1); cv2.rectangle(img,(130,45),(190,115),255,-1); cv2.line(img,(20,150),(220,150),255,5)
noise=np.random.default_rng(SEED).normal(0,18,img.shape).astype(np.int16)
noisy=np.clip(img.astype(np.int16)+noise,0,255).astype(np.uint8)
blur=cv2.GaussianBlur(noisy,(5,5),0); _,binary=cv2.threshold(blur,100,255,cv2.THRESH_BINARY)
count,labels,stats,centroids=cv2.connectedComponentsWithStats(binary)
contours,_=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print('components',count-1,'areas',stats[1:,cv2.CC_STAT_AREA].tolist())
assert count-1>=3
""",
        "independent": "Create contrast/noise/rotation source styles and report component-count accuracy and failure cases by source."
    },
    {
        "id": "N09", "file": "cnn_transfer_learning.ipynb", "sessions": "49-50",
        "title": "CNN and Offline Transfer-Learning Readiness",
        "target": "Train a tiny CNN and document the contract for rule-permitted offline pretrained assets.",
        "concepts": ["convolution/pooling shape flow", "augmentation only on training data", "freeze/unfreeze policy", "asset licence and hash"],
        "entry": ["Calculate one CNN output shape.", "Explain why validation augmentation differs.", "List metadata needed for a pretrained checkpoint."],
        "code": """import torch
from torch import nn
from torch.utils.data import TensorDataset,DataLoader
torch.manual_seed(SEED); device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
rng=np.random.default_rng(SEED); images=[]; labels=[]
for i in range(160):
    canvas=np.zeros((20,20),dtype=np.float32); label=i%2
    if label==0: canvas[6:14,6:14]=1
    else:
        yy,xx=np.ogrid[:20,:20]; canvas[(xx-10)**2+(yy-10)**2<=22]=1
    images.append(np.clip(canvas+rng.normal(0,.1,canvas.shape),0,1)); labels.append(label)
X=torch.tensor(np.array(images)[:,None]); y=torch.tensor(labels); train=DataLoader(TensorDataset(X[:120],y[:120]),batch_size=24,shuffle=True)
model=nn.Sequential(nn.Conv2d(1,8,3,padding=1),nn.ReLU(),nn.MaxPool2d(2),nn.Conv2d(8,12,3,padding=1),nn.ReLU(),nn.AdaptiveAvgPool2d(1),nn.Flatten(),nn.Linear(12,2)).to(device)
opt=torch.optim.Adam(model.parameters(),lr=.01); loss_fn=nn.CrossEntropyLoss()
for _ in range(3):
    for xb,yb in train:
        xb,yb=xb.to(device),yb.to(device); opt.zero_grad(); loss=loss_fn(model(xb),yb); loss.backward(); opt.step()
with torch.no_grad(): acc=(model(X[120:].to(device)).argmax(1).cpu()==y[120:]).float().mean().item()
print('accuracy',acc); assert acc>.8
""",
        "independent": "Compare with a teacher-provided locally cached checkpoint and record filename, SHA-256, source, licence, preprocessing, and frozen layers."
    },
    {
        "id": "N10", "file": "text_baseline_and_lstm.ipynb", "sessions": "51-53",
        "title": "Text Baseline and LSTM",
        "target": "Compare TF-IDF with a sequence model and analyse disagreement cases.",
        "concepts": ["tokenisation/vocabulary/padding", "simple baseline before deep model", "source and duplicate leakage", "slice errors by negation and length"],
        "entry": ["Tokenise one sentence.", "Explain padding and unknown token.", "Name a strong simple text baseline."],
        "code": """from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
rng=np.random.default_rng(SEED); pos=['clear','helpful','works']; neg=['confusing','broken','fails']; neutral=['lesson','model','code']; texts=[]; labels=[]
for _ in range(400):
    label=int(rng.random()>.5); words=list(rng.choice(neutral,3))+list(rng.choice(pos if label else neg,2)); rng.shuffle(words); texts.append(' '.join(words)); labels.append(label)
tr,va=train_test_split(np.arange(len(texts)),test_size=.25,stratify=labels,random_state=SEED)
pipe=Pipeline([('tfidf',TfidfVectorizer(ngram_range=(1,2))),('model',LogisticRegression(max_iter=1000))]).fit([texts[i] for i in tr],np.array(labels)[tr])
pred=pipe.predict([texts[i] for i in va]); print('TF-IDF F1',f1_score(np.array(labels)[va],pred))
""",
        "independent": "Build a compact LSTM or transformer classifier and compare disagreement slices for negation, length, source, and rare words."
    },
    {
        "id": "N11", "file": "audio_mel_classifier.ipynb", "sessions": "54-55",
        "title": "Audio Mel Classifier",
        "target": "Audit audio, generate Mel features, split by source, and classify reproducibly.",
        "concepts": ["waveform versus spectrogram", "Mel frequency scale", "speaker/device/source leakage", "ASR/TTS/classification are different tasks"],
        "entry": ["Define sample rate.", "Explain why random clip split may leak.", "State one label-preserving audio augmentation."],
        "code": """import librosa
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
sr=8000; t=np.arange(4000)/sr; rng=np.random.default_rng(SEED); rows=[]
for source in range(16):
    for j in range(6):
        label=(source+j)%2; freq=440 if label==0 else 880
        wave=np.sin(2*np.pi*freq*t)+rng.normal(0,.08,len(t))
        mel=librosa.feature.melspectrogram(y=wave.astype(np.float32),sr=sr,n_mels=20,n_fft=256,hop_length=128)
        db=librosa.power_to_db(mel,ref=np.max); rows.append((f'S{source:02d}',label,np.r_[db.mean(1),db.std(1)]))
X=np.stack([r[2] for r in rows]); y=np.array([r[1] for r in rows]); groups=np.array([r[0] for r in rows])
tr,va=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=SEED).split(X,y,groups))
pipe=Pipeline([('scale',StandardScaler()),('model',LogisticRegression(max_iter=1000))]).fit(X[tr],y[tr])
assert not(set(groups[tr]) & set(groups[va])); print('F1',f1_score(y[va],pipe.predict(X[va])))
""",
        "independent": "Add a source shift such as noise, gain, or sample-rate change and report performance by source and shift."
    },
    {
        "id": "N12", "file": "local_llm_multimodal.ipynb", "sessions": "56-57",
        "title": "Local LLM and Multimodal Offline Readiness",
        "target": "Validate local assets, structured output, modality baselines, and an offline execution record.",
        "concepts": ["no credentials or network dependency", "schema-constrained output", "text-only/image-only/fusion baselines", "asset hashes and licence record"],
        "entry": ["List three files in a local model package.", "Define a JSON output schema.", "Explain why fusion must beat trustworthy single-modality baselines."],
        "code": """import os, hashlib
MODEL_DIR=Path(os.environ.get('NOAI_LOCAL_MODEL_DIR','local_models/qwen'))
manifest={'path':str(MODEL_DIR),'exists':MODEL_DIR.exists(),'files':sorted(p.name for p in MODEL_DIR.glob('*'))[:20] if MODEL_DIR.exists() else []}
print(json.dumps(manifest,indent=2))
def validate_output(v):
    assert set(v)=={'label','confidence','reason'}
    assert v['label'] in {'true','false'} and 0<=v['confidence']<=1 and len(v['reason'])<=160
validate_output({'label':'true','confidence':.78,'reason':'Caption and measured shape agree.'})
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
rng=np.random.default_rng(SEED); n=250; actual=rng.integers(0,3,n); stated=np.where(rng.random(n)>.5,actual,rng.integers(0,3,n)); size=rng.integers(0,2,n); y=(actual==stated).astype(int)
for name,X in [('text',np.c_[stated,size]),('image',np.c_[actual,size]),('fusion',np.c_[stated,actual,size])]:
    m=LogisticRegression(max_iter=1000).fit(X[:180],y[:180]); print(name,f1_score(y[180:],m.predict(X[180:])))
""",
        "independent": "Run a teacher-provided local Qwen smoke test with networking disabled and record hashes, versions, memory, latency, deterministic settings, parsed JSON, and fallback behaviour."
    },
]


def md(text: str):
    return nbf.v4.new_markdown_cell(textwrap.dedent(text).strip() + "\n")


def code(text: str):
    return nbf.v4.new_code_cell(textwrap.dedent(text).strip() + "\n")


for lesson in LESSONS:
    concepts = "\n".join(f"- {item}" for item in lesson["concepts"])
    entry = "\n".join(f"{i}. {item}" for i, item in enumerate(lesson["entry"], 1))
    nb = nbf.v4.new_notebook(
        metadata={
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
            "course": {"sessions": lesson["sessions"], "seed": 42, "runtime": "CPU-safe; no network downloads"},
        }
    )
    nb.cells = [
        md(f"# {lesson['id']} — {lesson['title']}\n\n**Sessions:** {lesson['sessions']}  \n**Learning target:** {lesson['target']}"),
        code(HEADER),
        md(f"## Essential content\n{concepts}"),
        md(f"## Entry check\n{entry}"),
        code(lesson["code"]),
        md("## Guided practice\nAnnotate the code, predict shapes/outputs before execution, then change one input and explain the result."),
        md(f"## Independent transfer\n{lesson['independent']}"),
        md("## Exit evidence\n- completed worksheet answers;\n- one independently produced artifact;\n- one error and correction;\n- one oral explanation;\n- AI-use note when applicable;\n- meaningful Git commit."),
        md("## Fresh-run checklist\n- [ ] Restart kernel and run all cells in order.\n- [ ] Assertions pass.\n- [ ] Versions and seed are recorded.\n- [ ] No secrets, hidden labels, or downloaded assets are committed.\n- [ ] Required output is reproducible from relative paths."),
    ]
    nbf.write(nb, OUT / lesson["file"])

lines = [
    "# Ready-to-Teach Starter Notebooks", "",
    "Generated by `scripts/generate_ready_notebooks.py`. All notebooks are CPU-safe, deterministic, and avoid network downloads.", "",
    "| ID | Notebook | Sessions |", "|---|---|---|",
]
for lesson in LESSONS:
    lines.append(f"| {lesson['id']} | [{lesson['file']}]({lesson['file']}) | {lesson['sessions']} |")
(OUT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Generated {len(LESSONS)} notebooks in {OUT}")
