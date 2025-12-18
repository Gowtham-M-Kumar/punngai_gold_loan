from django.db import models

# =========================
# CUSTOMER
# =========================
class Customer(models.Model):
    name = models.CharField(max_length=100)
    
    mobile_primary = models.CharField(max_length=10, unique=True)
    mobile_secondary = models.CharField(max_length=10, blank=True)

    email = models.EmailField(blank=True)
    address = models.TextField()

    aadhaar_number = models.CharField(max_length=12, unique=True)

    profession = models.CharField(max_length=100)

    nominee_name = models.CharField(max_length=100)
    nominee_mobile = models.CharField(max_length=10)

    photo = models.ImageField(upload_to="customers/photos/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.mobile_primary})"


# =========================
# LOAN
# =========================
class Loan(models.Model):

    STATUS_DRAFT = "draft"
    STATUS_ACTIVE = "active"
    STATUS_CLOSED = "closed"

    STATUS_CHOICES = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_ACTIVE, "Active"),
        (STATUS_CLOSED, "Closed"),
    ]

    lot_number = models.CharField(max_length=20, unique=True)
    loan_number = models.CharField(max_length=20, unique=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="loans"
    )

    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    price_per_gram = models.DecimalField(max_digits=8, decimal_places=2)

    approved_grams = models.DecimalField(max_digits=6, decimal_places=3)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_number


# =========================
# GOLD ITEM
# =========================
class GoldItem(models.Model):

    CARAT_CHOICES = [
        (18, "18K"),
        (20, "20K"),
        (22, "22K"),
        (24, "24K"),
    ]

    loan = models.ForeignKey(
        Loan,
        on_delete=models.CASCADE,
        related_name="items"
    )

    item_name = models.CharField(max_length=100)
    carat = models.IntegerField(choices=CARAT_CHOICES)

    gross_weight = models.DecimalField(max_digits=6, decimal_places=3)
    approved_net_weight = models.DecimalField(max_digits=6, decimal_places=3)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.item_name


# =========================
# GOLD ITEM IMAGE
# =========================
class GoldItemImage(models.Model):
    gold_item = models.ForeignKey(
        GoldItem,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to="gold_items/images/")


# =========================
# LOAN DOCUMENT
# =========================
class LoanDocument(models.Model):

    DOCUMENT_AADHAAR = "aadhaar"
    DOCUMENT_PAN = "pan"
    DOCUMENT_PHOTO = "photo"
    DOCUMENT_OTHER = "other"

    DOCUMENT_CHOICES = [
        (DOCUMENT_AADHAAR, "Aadhaar"),
        (DOCUMENT_PAN, "PAN"),
        (DOCUMENT_PHOTO, "Photo"),
        (DOCUMENT_OTHER, "Other"),
    ]

    loan = models.ForeignKey(
        Loan,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    document_type = models.CharField(
        max_length=20,
        choices=DOCUMENT_CHOICES
    )

    other_name = models.CharField(max_length=100, blank=True)

    image = models.ImageField(upload_to="loan_documents/")
