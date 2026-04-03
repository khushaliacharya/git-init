# Contributing to the Project

Thank you for your interest in contributing to our project! We appreciate your efforts in making the project better. Below are the guidelines to help you get started.

## Development Setup
1. **Clone the repository:**  
   `git clone https://github.com/khushaliacharya/git-init.git`

2. **Install dependencies:**  
   For Python/Flask:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
   For React/JavaScript:
   ```bash
   cd frontend
   npm install
   ```

3. **Run the development server:**  
   For Python/Flask:
   ```bash
   flask run
   ```
   For React:
   ```bash
   npm start
   ```

## Testing Guidelines
- Write tests for new features and bug fixes.
- Ensure all tests pass before submitting your contributions.
- Use `pytest` for Python tests and `Jest` for React tests.

## Code Standards
- **Python/Flask:**
  - Follow PEP 8 style guide.
  - Use descriptive variable names.
  - Avoid unnecessary complexity.

- **React/JavaScript:**
  - Follow Airbnb JavaScript style guide.
  - Keep components small and focused.
  - Use functional components and hooks whenever possible.

## Commit Format
- Use the [Conventional Commits](https://www.conventionalcommits.org/) format for commit messages:
  - `type(scope): subject`
  - Example: `feat(tests): implement user registration tests`

## Pull Request Process
1. **Create a new branch:**  
   Use a descriptive name for your branch, e.g., `feature/add-login` or `bugfix/fix-typo`.

2. **Make your changes and commit:**  
   Following the commit format mentioned above.

3. **Push your branch:**  
   `git push origin your-branch-name`

4. **Create a pull request:**  
   Go to the repository on GitHub and click on "New Pull Request".

5. **Request a review:**  
   Tag relevant team members for review.

6. **Address feedback:**  
   Make necessary changes based on the feedback received before merging.  

Thank you again for your contributions! 

Happy coding!