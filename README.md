# SimpleBEV (Colab 워크플로)

이 저장소는 NuScenes mini로 SimpleBEV를 Colab에서 실행한 워크플로를
재현 가능하게 정리한 것입니다. 핵심 실행 흐름은 `notebook/simpleBEV.ipynb`에 있고,
이 레포에는 필요한 문서와 패치 스크립트만 포함합니다.

## 빠른 시작 (Colab)

1) `notebook/simpleBEV.ipynb`를 Colab에서 엽니다.
2) 런타임을 GPU로 설정합니다.
3) 구글 드라이브를 마운트합니다.
4) NuScenes 데이터 위치를 확인합니다.
   - `/content/drive/MyDrive/data/sets/nuscenes`
   - 필수 폴더: `maps/`, `samples/`, `sweeps/`, `v1.0-mini/`
   - 메타데이터: `*.pkl`
5) 셀을 위에서 아래로 순서대로 실행합니다.

## 디렉터리 구조

```text
.
├─ notebook/
│  └─ simpleBEV.ipynb
└─ results/
   └─ mini/
      ├─ lidar_nonaug/
      │  ├─ before/png/sample_vis_000/
      │  │  ├─ rgb/
      │  │  ├─ lidar/
      │  │  └─ seg/
      │  │     ├─ et/
      │  │     └─ gt/
      │  └─ after/png/sample_vis_000/ (sample_vis_001, sample_vis_002 동일)
      │     ├─ rgb/
      │     ├─ lidar/
      │     └─ seg/
      │        ├─ et/
      │        └─ gt/
      ├─ lidar_aug/
      │  └─ png/sample_vis_000/ (sample_vis_001, sample_vis_002 동일)
      │     ├─ rgb/
      │     ├─ lidar/
      │     └─ seg/
      │        ├─ et/
      │        └─ gt/
      └─ radar_nonswp/
         └─ png/sample_vis_000/ (sample_vis_001, sample_vis_002 동일)
            ├─ rgb/
            ├─ radar/
            └─ seg/
               ├─ et/
               └─ gt/
```

## 의존성

노트북에서 직접 설치하지만, 고정 버전 목록을 `requirements.txt`에
정리해 두었습니다.

```bash
pip install -r requirements.txt
```

## SimpleBEV 패치

상류(simple_bev) 코드에서 발생하는 dtype/지도 로드 오류를 피하기 위한
패치가 필요합니다. 노트북과 동일한 변경을 스크립트로 제공합니다.

```bash
python scripts/patch_simple_bev.py --repo /content/simple_bev
```

## Citation

If you use this code for your research, please cite:

Simple-BEV: What Really Matters for Multi-Sensor BEV Perception?. Adam W. Harley, Zhaoyuan Fang, Jie Li, Rares Ambrus, Katerina Fragkiadaki. In arXiv:2206.07959.

Bibtex:

```bibtex
@inproceedings{harley2022simple,
  title={Simple-{BEV}: What Really Matters for Multi-Sensor BEV Perception?},
  author={Adam W. Harley and Zhaoyuan Fang and Jie Li and Rares Ambrus and Katerina Fragkiadaki},
  booktitle={arXiv:2206.07959},
  year={2022}
}
```

## 참고

- 데이터/체크포인트/로그는 git에서 제외합니다(`.gitignore`).
- 시각화 결과 PNG는 `results/mini` 아래에 설정별로 분리해 저장합니다.
- `seg/et`와 `seg/gt`를 나란히 두어 비교가 쉽도록 구성했습니다.
- radar 실험(`radar_nonswp`)은 `radar/` 폴더를 포함합니다.
- 이 레포는 Colab 전용 사용을 목표로 합니다.
