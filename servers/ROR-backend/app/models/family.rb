class Family < ApplicationRecord
    has_many :users
    
    validates :family_name, presence: true

  end