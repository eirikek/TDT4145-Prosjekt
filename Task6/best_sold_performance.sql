SELECT T.Navn, F.Dato, COUNT(B.BillettID) AS AntallSolgteBilletter
FROM TeaterStykke AS T
INNER JOIN Forestilling AS F ON F.TeaterStykkeID = T.TeaterStykkeID
INNER JOIN Billett AS B ON B.ForestillingDato = F.Dato AND B.TeaterStykkeID = F.TeaterStykkeID
GROUP BY T.Navn, F.Dato
ORDER BY AntallSolgteBilletter DESC
