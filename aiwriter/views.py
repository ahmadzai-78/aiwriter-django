from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import DocumentForm
from .models import Document
from xhtml2pdf import pisa


def writer_view(request):
    generated_text = None

    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['client_name']
            service = form.cleaned_data['service']
            amount = form.cleaned_data['amount']
            style = form.cleaned_data['style']

            # Texte simulé selon le style
            if style == "formel":
                generated_text = f"""Madame, Monsieur {name},

Nous vous confirmons que la prestation '{service}' sera réalisée pour un montant de {amount} €.

Nous restons à votre disposition pour toute information complémentaire.

Cordialement,
Votre entreprise."""
            elif style == "commercial":
                generated_text = f"""Bonjour {name},

Nous sommes ravis de vous proposer notre prestation : '{service}', au tarif de {amount} €.

N'hésitez pas à revenir vers nous pour valider ce devis.

À très bientôt !
L’équipe commerciale."""
            else:  # amical
                generated_text = f"""Salut {name} 👋,

Voici les infos pour la prestation : '{service}' → {amount} €.

Dis-moi si ça te va, et on démarre dès que tu veux 😄

À bientôt,
Ton prestataire préféré."""

            # Enregistrement
            Document.objects.create(
                client_name=name,
                service=service,
                amount=amount,
                style=style,
                generated_text=generated_text
            )
    else:
        form = DocumentForm()

    return render(request, 'writer_form.html', {
        'form': form,
        'generated_text': generated_text
    })


def generate_pdf(request):
    if request.method == "POST":
        template = get_template("pdf_template.html")
        context = {
            "client_name": request.POST.get("client_name"),
            "service": request.POST.get("service"),
            "amount": request.POST.get("amount"),
            "style": request.POST.get("style"),
            "generated_text": request.POST.get("generated_text"),
        }

        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="document.pdf"'
        pisa.CreatePDF(html, dest=response)
        return response

    return HttpResponse("Méthode non autorisée", status=405)
