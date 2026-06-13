# Management of Transaction Integrity (backup and rollback capability)

> Source: https://xanthus-consulting.com/IntelliGrid_Architecture/New_Technologies/Tech_Management_of_Transaction_Integrity_(backup_and_rollback_cap.htm

---

*![](../images/IntelliGridlogo.jpg)*

*IntelliGrid Architecture*

![](../images/EPRI-head01-alt.jpg)

### Management of Transaction Integrity (backup and rollback capability)

Many
systems require one-step transactions, where if the transaction fails for some
reason, the results must be either ignored or rolled back. Two-step
transactions are even more complex, since sometimes the results of the second
transaction must also roll back the results of the first transaction.

Utility
operations systems have not often needed this capability except peripherally.
For example in updating the SCADA database, roll back to a previous version is
needed if some error was introduced into the updated version of the database.
However, this type of capability is certainly required in the market
operations, and increasingly in other control center functions.

Two-step
transactions and roll-back have been implemented in a number of products.

**Keywords:**keywords
