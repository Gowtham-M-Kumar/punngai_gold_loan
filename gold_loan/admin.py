from django.contrib import admin
from .models import (
    Customer,
    Loan,
    GoldItem,
    GoldItemImage,
    LoanDocument
)

# =========================
# INLINE MODELS
# =========================

class GoldItemImageInline(admin.TabularInline):
    model = GoldItemImage
    extra = 0


class GoldItemInline(admin.TabularInline):
    model = GoldItem
    extra = 0


class LoanDocumentInline(admin.TabularInline):
    model = LoanDocument
    extra = 0


# =========================
# CUSTOMER ADMIN
# =========================

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "mobile_primary",
        "aadhaar_number",
        "profession",
        "nominee_name",
        "created_at",
    )

    search_fields = (
        "name",
        "mobile_primary",
        "aadhaar_number",
    )

    list_filter = ("profession",)
    ordering = ("-created_at",)


# =========================
# LOAN ADMIN
# =========================

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "loan_number",
        "lot_number",
        "customer",
        "total_amount",
        "interest_rate",
        "status",
        "created_at",
    )

    search_fields = (
        "loan_number",
        "lot_number",
        "customer__name",
        "customer__mobile_primary",
    )

    list_filter = ("status",)
    ordering = ("-created_at",)

    inlines = [
        GoldItemInline,
        LoanDocumentInline,
    ]


# =========================
# GOLD ITEM ADMIN
# =========================

@admin.register(GoldItem)
class GoldItemAdmin(admin.ModelAdmin):
    list_display = (
        "item_name",
        "loan",
        "carat",
        "gross_weight",
        "approved_net_weight",
    )

    list_filter = ("carat",)
    inlines = [GoldItemImageInline]


# =========================
# LOAN DOCUMENT ADMIN
# =========================

@admin.register(LoanDocument)
class LoanDocumentAdmin(admin.ModelAdmin):
    list_display = (
        "loan",
        "document_type",
        "other_name",
    )
