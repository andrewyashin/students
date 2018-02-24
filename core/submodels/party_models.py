from django.db import models


class ContactType(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=128)
    template = models.CharField(max_length=64)
    infoText = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class PartyType(models.Model):
    name = models.CharField(max_length=45)
    caption = models.CharField(max_length=60)
    infoText = models.CharField(max_length=255, blank=True, null=True)


class Party(models.Model):
    STATE_TYPE = (
        ('ACT', 'Active'),
        ('SUS', 'Suspended'),
        ('DEL', 'Deleted')
    )
    partyType = models.ForeignKey(PartyType, on_delete=models.CASCADE)
    state = models.CharField(max_length=5, choices=STATE_TYPE)
    infoText = models.CharField(max_length=255, blank=True, null=True)


class PartyContact(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, blank=True, null=True)
    contactType = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    contact = models.CharField(max_length=512)
    infoText = models.CharField(max_length=255, blank=True, null=True)


class RelationshipType(models.Model):
    caption = models.CharField(max_length=64)
    srcDef = models.CharField(max_length=45)
    dstDef = models.CharField(max_length=45)
    infoText = models.CharField(max_length=255, blank=True, null=True)


class Role(models.Model):
    caption = models.CharField(max_length=128)
    roleFlag = models.CharField(max_length=8)
    infoText = models.CharField(max_length=255, blank=True, null=True)


class PartyHasRole(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    startDate = models.DateField
    endDate = models.DateField
    infoText = models.CharField(max_length=255, blank=True, null=True)


class Relationship(models.Model):
    caption = models.CharField(max_length=64)
    relationshipType = models.ForeignKey(RelationshipType, on_delete=models.CASCADE)
    srcParty = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="srcParty")
    destParty = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="destParty")
    startDate = models.DateField
    endDate = models.DateField