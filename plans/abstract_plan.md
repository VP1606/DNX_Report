# Abstract Plan

## Structure

Inpsired from the Oxford Guide to write Abstracts.

[URL](https://lifelong-learning.ox.ac.uk/about/writing-abstracts)

### Numbered Plan

1. Context of the Problem (Background)
2. Motivation of why the project is needed (Motivation)
3. Main direction/hypotheses of the project (Research issues/problems/questions/hypotheses)
4. Method, eg. "we propose DectectorNX using xyz" (Method)
5. Summary of headline results (Results)
6. Conclusion of the Project (Conclusion)
7. Contribution to the Field of Study

### Page Limit

300 words.

## Ideas

The following ideas and their numbering order match the numbered plan detailed in the previous section:

1. Euro NCAP / Legal Bodies: mandating cars to adopt more technology. Ultimately, it will lead to them having systems that are capable of full spatial understanding.

2. Simply scaling conventional dense DNNs to meet growing legal requirements on GPU‑class accelerators is increasingly unsustainable for mass‑market autonomous vehicles, motivating ultra‑efficient architectures such as spiking neural networks for tasks like vehicle detection.

3. Develop the first SNN for direct vehicle detection application, using the ETRAM dataset (it is the first SNN developed on this dataset). Study the implications of the quantisation error that SNNs inherently suffer from in this application, and the power benefits (theoretical and realised) that can be expected using a philosophy of activation sparsity.
We aim to understand/show the cost of the spiking paradigm.

4. We propose DetectorNX, with an SNN and CNN counterpart using 1:1 architectural parity. The SNN was NOT developed using ANN->SNN conversion, but from the ground up with activation sparsity being the lead philosophy to drive power efficiency.

5. mAP50, IOU, Recall > 0.5, Parity of IOU/mAP between CNN and SNN, Power Savings (theoretical and realised on A100 GPU). SNN demonstrates superior confidence at low-confidence regions.

6. We've established cost of the losses that can be expected by switching to a fully ground-up SNN over an CNN due to inherent losses (ie. quantization, LIF dynamics) through the SNN-CNN parity results. We have developed a solid foundation for future work to develop a full SNN to perform vehicle detection and be used in future ADAS systems, with significant power benefit.

7. (The bullet points below)

- Quantified the cost of the spiking paradigm by using identical models, data and training through the CNN-SNN parity.

- shown that the quantization error (in this implementation) acts as a global ceiling instead of a scaled one.

- SNN demonstrates superior confidence at low-confidence regions.

- Provides a baseline of an SNN for ETRAM, and future work to develop it further to close the gap to competitor models.

