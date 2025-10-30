restart policy- Onfailure, Never, always
----------------------
reclaim policy-retain, delete, recycle
--------------------
imagepull policy- always, ifpresent, Never
----------------


| Policy                     | Description                                  | Data Retained? | Manual Action Needed? | Use Case                          |
| -------------------------- | -------------------------------------------- | -------------- | --------------------- | --------------------------------- |
| **Retain**                 | Keeps PV and data after PVC deletion         | ✅ Yes          | ✅ Yes                 | Production backups, data recovery |
| **Delete**                 | Deletes PV and backend storage automatically | ❌ No           | ❌ No                  | Dynamic, short-lived environments |
| **Recycle** *(deprecated)* | Wipes data and reuses PV                     | ❌ No           | ❌ No                  | Legacy clusters only              |


