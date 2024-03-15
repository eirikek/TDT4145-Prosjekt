SELECT S.Navn AS SkueSpillerNavn, Rolle.Navn AS RolleNavn, TeaterStykke.Navn AS TeaterStykkeNavn
FROM Skuespiller AS S
INNER JOIN Spiller ON S.AnsattID = Spiller.AnsattID
INNER JOIN Rolle ON Spiller.RolleID = Rolle.RolleID
INNER JOIN DeltarI ON Rolle.RolleID = DeltarI.RolleID
INNER JOIN TeaterStykke ON DeltarI.TeaterStykkeID = TeaterStykke.TeaterStykkeID
GROUP BY S.AnsattID, Rolle.RolleID
