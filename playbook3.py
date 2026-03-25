---
- name: Install Java on EC2 Linux
  hosts: all
  become: yes
  tasks:
    - name: Update yum package cache
      yum:
        update_cache: yes

    - name: Install OpenJDK 11
      yum:
        name: java-11-amazon-corretto-headless # Or java-1.8.0-openjdk-devel
        state: present

    - name: Verify Java installation
      command: java -version
      register: java_version

    - name: Display Java version
      debug:
        var: java_version.stdout
