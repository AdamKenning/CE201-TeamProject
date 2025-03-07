# Test report  

Introduction
An integration test on the project's database serves as the basis for this test report.  This testing's main goal was to confirm that different modules—such as data handling, authentication, and user interactions integrate seamlessly to offer a smooth user experience.

1.	Objectives of Integration Testing
The main goals of integration testing for the application include:
- Ensuring seamless interaction between different modules (e.g., models, views, forms, and authentication system).
- Validating data consistency when transferred between components.
- Checking that authenticated users can access and modify child records appropriately.
- Ensuring proper error handling and redirects for unauthorized access attempts.
- Verifying correct functionality of dashboard statistics and tracking pages.

2.	Test Environment and Tools
To ensure consistency and replicate real-world settings, the integration testing was carried out in a controlled setting.  The environment's specifics are as follows:
- Framework: Django (Python-based web framework)
- Database: SQLite (used for testing, PostgreSQL in production)
- Backend Language: Python (Django models, views, forms)
- Frontend: HTML, CSS, JavaScript (for rendering UI elements)

3.	Test Plan
The integration testing was structured around the following key test scenarios:

3.1 Model Integration Tests
The objective for the model integration tests were to ensure data integrity and relationships between different models (e.g., “User”, “Child”, “Profile”, “FamilyAssociation”).

 | Test Case Description | Expected Result | Result |
| Verify that a child can be successfully associated with a parent | The child should be linked to the parent in the database | Pass |
| Ensure child data (first name, last name, DOB) is stored correctly | Retrieved data should match input values | Pass |
| Verify that deleting a parent account does not delete child records | Child records should remain intact | Pass |

3.2 View Integration Tests
The objective for the view integration tests is to ensure that views render correctly and return expected responses based on user authentication and data availability.

| Test Case Description | Expected Result | Result 
| Ensure that the dashboard displays the child’s name correctly | Child’s name appears on the dashboard | Pass |
| Test if an unauthenticated user is redirected when accessing protected pages | User should be redirected to login page | Pass |

3.3 Form Handling Tests
The Objective of form handling tests is to ensure that forms validate and submit data correctly without errors.

| Test Case Description | Expected Result | Result |
| Ensure the child creation form saves valid data correctly | Child record should be created |  Pass |
| Test form validation with missing required fields | Form should be invalid | Pass |
| Verify incorrect share codes do not add children | Child should not be added | Pass |

4.4 Authentication and Authorization Tests
The Objective of authentication and autherization tests is to ensure secure authentication and access control mechanisms.

| Test Case Description | Expected Outcome | Status |
| Ensure only authenticated users can access tracking pages | Redirect to login page | Pass |
| Test login functionality with valid credentials | User should be logged in successfully | Pass |
| Check if logging out prevents access to protected pages | Redirect to login page | Pass |

---

5. Test Execution Summary
| Total Tests | Passed | Failed 
| 12|                 | 12 |    | 0 |

Overall, all the integration tests were passed and successful and no major issues were found during the testing. 

6. Findings
The integration between models and views is functioning as expected. Child records are correctly associated with parents, and tracking pages display relevant data without inconsistencies. The authentication system prevents unauthorized access. Users must be logged in to view and update child records. Form validation is working correctly. Incorrect data is not accepted, and required fields must be filled before submission. Redirects and session management are properly handled. Users selecting a child in one session see the correct data across all tracking pages.

Conclusion
The integration testing for the application was successful, with all tests passing and no major issues identified. The system components interact correctly, ensuring a seamless user experience for parents tracking their child’s activities.


