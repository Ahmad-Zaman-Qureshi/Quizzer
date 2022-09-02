from django.db import models

# Create your models here.
class QuizCode(models.Model):
    userid=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)
    date=models.CharField(max_length=200,null=True)
    quiz_topic=models.CharField(max_length=200,null=True)
    
    
class QuizData(models.Model):
    question=models.CharField(max_length=200,null=True)
    wrongansw1=models.CharField(max_length=200,null=True)
    wrongansw2=models.CharField(max_length=200,null=True)
    wrongansw3=models.CharField(max_length=200,null=True)
    wrongansw4=models.CharField(max_length=200,null=True)
    correctansw=models.CharField(max_length=200,null=True)
    qquizcode=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
        
class StudentData(models.Model):
    name=models.CharField(max_length=200,null=True)
    rollno=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    confirmpassword=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class MCQAttemptStudent(models.Model):
    name=models.CharField(max_length=200,null=True)
    rollno=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


class StudentMarks(models.Model):
    rollno=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)
    marks=models.CharField(max_length=200,null=True)
    percentagee=models.CharField(max_length=200,null=True)

class QuizCodeFB(models.Model):
    userid=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)
    date=models.CharField(max_length=200,null=True)
    quiz_topic=models.CharField(max_length=200,null=True)


class QuizDataFB(models.Model):
    question=models.CharField(max_length=2000,null=True)
    correctans=models.CharField(max_length=20,null=True)
    qquizcode=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.question


class FBAttemptStudent(models.Model):
    name=models.CharField(max_length=200,null=True)
    rollno=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
class UploadFileModel(models.Model):
    title = models.CharField(max_length=50,null=True)
    file = models.FileField(upload_to='documents',null=True)

    def __str__(self):
        return self.file

class QuizDataTF(models.Model):
    question=models.CharField(max_length=2000,null=True)
    false=models.CharField(max_length=20,null=True)
    true=models.CharField(max_length=20,null=True)
    correctans=models.CharField(max_length=20,null=True)
    qquizcode=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.question

class QuizCodeTF(models.Model):
    userid=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)
    date=models.CharField(max_length=200,null=True)
    quiz_topic=models.CharField(max_length=200,null=True)

class TFAttemptStudent(models.Model):
    name=models.CharField(max_length=200,null=True)
    rollno=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)