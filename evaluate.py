import os
from dotenv import load_dotenv
from pawpal_system import Owner, Pet, Task, Scheduler
from ai_planner import generate_care_plan
from datetime import date, time

load_dotenv()

print("=" * 50)
print("PawPal+ AI Evaluation Script")
print("=" * 50)

results = []

def run_test(test_name, pet_name, species, breed, age, tasks_data):
    print(f"\n Test: {test_name}")
    owner = Owner("TestOwner")
    pet = Pet(name=pet_name, breed=breed, species=species, age=age)
    owner.add_pet(pet)
    for task_type, task_time in tasks_data:
        task = Task(task_type=task_type, date=date.today(), time=task_time, pet=pet)
        pet.add_task(task)
    plan = generate_care_plan(pet_name, species, breed, age, pet.get_pending_tasks())
    passed = len(plan) > 50 and "Sorry" not in plan
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"Status: {status}")
    print(f"AI Response Preview: {plan[:150]}...")
    results.append((test_name, passed))
    return passed

run_test("Golden Retriever with walk", "Buddy", "Dog", "Golden Retriever", 3,
         [("Walk", time(14, 0))])

run_test("Husky with medication", "Alaska", "Dog", "Husky", 6,
         [("Medication", time(9, 0))])

run_test("Cat with multiple tasks", "Whiskers", "Cat", "Siamese", 2,
         [("Feeding", time(8, 0)), ("Grooming", time(15, 0))])

print("\n" + "=" * 50)
print("EVALUATION SUMMARY")
print("=" * 50)
passed = sum(1 for _, p in results if p)
print(f"Tests passed: {passed}/{len(results)}")
for name, p in results:
    print(f"  {'✅' if p else '❌'} {name}")