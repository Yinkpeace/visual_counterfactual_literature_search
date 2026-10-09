"""Visual-scope triage and suggested categories, not final eligibility decisions."""
import re

QUERIES = (
    'counterfactual visual', 'counterfactual image', 'counterfactual video',
    'counterfactual computer vision', 'counterfactual medical imaging',
    'counterfactual vision language', 'counterfactual visual question answering',
    'counterfactual scene',
)
COUNTERFACTUAL = re.compile(r'\bcounter[- ]?factual(?:s|ity)?\b', re.I)
VISUAL = re.compile(
    r'\b(?:visual(?:ly)?|vision|images?|videos?|pixels?|photographs?|radiolog\w*|'
    r'medical imag\w*|x[- ]ray|mri|retinal|histopatholog\w*|'
    r'object detection|image segmentation|scene(?:s)?|vqa|vlm(?:s)?)\b', re.I)
SECONDARY = re.compile(r'\b(?:survey|systematic review|literature review|scoping review|tutorial)\b', re.I)
PURPOSES = {
    'explanation': r'explan\w*|interpret\w*',
    'learning': r'train\w*|representation learning|data augmentation',
    'auditing': r'audit\w*|bias|fairness|diagnos\w*',
    'benchmarking': r'benchmark\w*|evaluat\w*|test set',
    'mitigation': r'mitigat\w*|repair\w*|privacy|debias\w*',
    'visual_editing': r'edit\w*|inpaint\w*|image synthesis|image generation',
}
ARTIFACTS = {
    'image_or_video': r'images?|videos?|pixels?',
    'region_or_mask': r'patch\w*|regions?|masks?|saliency',
    'latent_or_concept': r'latent|concept\w*|attributes?',
    'visual_scene': r'scenes?|visual states?|objects?',
    'vision_language': r'vision[- ]language|visual question|captions?|vqa|vlm',
}


def suggested_tags(text, patterns):
    return ';'.join(name for name, pattern in patterns.items()
                    if re.search(r'\b(?:' + pattern + r')\b', text, re.I))


def linked_visual_evidence(text):
    """Require nearby mentions in a sentence; never infer scope from venue."""
    for sentence in re.split(r'(?<=[.!?])\s+|\n', text):
        for cf in COUNTERFACTUAL.finditer(sentence):
            if VISUAL.search(sentence[max(0, cf.start() - 120):cf.end() + 120]):
                return sentence[max(0, cf.start() - 180):cf.end() + 300]
    return ''


def screen(record, full_text=''):
    title, abstract = record.get('title', ''), record.get('abstract', '')
    metadata = title + '. ' + abstract
    evidence = linked_visual_evidence(metadata)
    if SECONDARY.search(title):
        decision, reason = 'background', 'secondary_literature'
    elif evidence:
        decision, reason = 'candidate', 'linked_visual_counterfactual_evidence'
    elif not abstract.strip() and COUNTERFACTUAL.search(title):
        decision, reason = 'manual_review', 'abstract_unavailable'
    elif not COUNTERFACTUAL.search(metadata):
        decision, reason = 'excluded', 'no_counterfactual_evidence_in_metadata'
    elif not VISUAL.search(metadata):
        decision, reason = 'excluded', 'no_visual_evidence_in_metadata'
    else:
        decision, reason = 'manual_review', 'visual_centrality_uncertain'
    # Incidental full-text or reference-list mentions require human confirmation.
    extra = linked_visual_evidence(full_text) if full_text else ''
    if extra and decision == 'excluded':
        decision, reason = 'manual_review', 'full_text_visual_evidence_needs_confirmation'
    return {
        'screening_decision': decision, 'screening_reason': reason,
        'evidence_excerpt': evidence or extra,
        'suggested_purposes': suggested_tags(metadata, PURPOSES) if decision in ('candidate', 'manual_review') else '',
        'suggested_artifacts': suggested_tags(metadata, ARTIFACTS) if decision in ('candidate', 'manual_review') else '',
    }
